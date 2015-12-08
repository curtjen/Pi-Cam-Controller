#!/usr/local/bin/python

# Import 'os' library for using operating system commandments
import os

# Create main folder for storing repos
user_dir = os.path.expanduser('~')
top_dir = "%s/git_repos" % user_dir

if os.path.exists(top_dir):
    print "%s exists" % top_dir
else:
    os.makedirs(top_dir)
    print "%s created" % top_dir


# Set up locales
os.system("sudo export LANGUAGE=en_US.UTF-7 && sudo export LANG=en_US.UTF-7 && sudo export LC_ALL=en_US.UTF-7 && sudo locale-gen en_US.UTF-7 && sudo dpkg-reconfigure locales")

# Install autoreconf
os.system("sudo apt-get install dh-autoreconf")

# Install dependencies that can be through apt-get
os.system("sudo apt-get install libpopt-dev")


# The list of libraries (list in order of dependency with dependents first)
libraries = [
    {
        "name": "https://github.com/gphoto/libgphoto2.git",
        "folder": "libgphoto2",
        "ops": ""
    },
    {
        "name": "https://github.com/gphoto/gphoto2",
        "folder": "gphoto2",
        "ops": ""
    },
    {
        "name": "git://git.videolan.org/x264",
        "folder": "x264",
        "ops": "--host=arm-unknown-linux-gnueabi --enable-static --disable-opencl"
    },
    {
        "name": "git://source.ffmpeg.org/ffmpeg.git",
        "folder": "ffmpeg",
        "ops": "--arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree"
    }
]

# Run the compile steps
def run_compile(lib):
    ops = lib['ops']

    # Run configure > Run make as sudo > Run make install as sudo
    os.system("./configure %s && sudo make && sudo make install" % ops)


# Download/Clone the things
def get_git_repos():
    for lib in libraries:
        name   = lib['name']
        folder = lib['folder']
        dir_path = "%s/%s" % (top_dir, folder)
        os.system("git clone %s %s" % (name, dir_path))


# Compile the libraries
def compile_libs():
    for lib in libraries:
        folder   = lib['folder']
        dir_path = "%s/%s" % (top_dir, folder)
        os.chdir(dir_path)

        if os.path.exists("configure"):
            print "%s/configure exists!" % dir_path

            run_compile(lib)

        elif os.path.exists("configure.ac"):
            print "%s/configure.ac exists!" % dir_path

            os.system("autoreconf -is")
            run_compile(lib)

        else:
            print "configure does not exist at %s." % dir_path


# Run steps
# Step 1: Download the things
get_git_repos()

# Step 2: Compile the libraries
compile_libs()
