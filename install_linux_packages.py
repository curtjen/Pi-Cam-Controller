#!/usr/bin/python

import os

# Create top level directory for storing repos
user_dir = os.path.expanduser('~')
top_dir = '%s/git_repos' % user_dir

if os.path.exists(top_dir):
    print "%s exists" % top_dir
else:
    os.makedirs(top_dir)
    print "%s created" % top_dir

# Set up locales
os.system("export LANGUAGE=en_US.UTF-8 && export LANG=en_US.UTF-8 && sudo export LC_ALL=en_US.UTF-8 && sudo locale-gen en_US.UTF-8 && sudo dpkg-reconfigure locales")

# Install autoreconf
print "Installing autoreconf..."
os.system("sudo apt-get -y install dh-autoreconf")

# Install dependencies that can be obtained through apt-get
os.system("sudo apt-get install libpopt-dev")

# Install gphoto2
os.system("sudo apt-get -y install gphoto2")

# Install imagemagick
os.system("sudo apt-get install imagemagick")

libraries = [
    {
        "repo": "git://git.videolan.org/x264",
        "folder": "x264",
        "opts": "--host=arm-unknown-linux-gnueabi --enable-static --disable-opencl"
    },
    {
        "repo": "git://source.ffmpeg.org/ffmpeg.git",
        "folder": "ffmpeg",
        "opts": "--arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree"
    }
]
    
    
# Run the compilation steps
def run_compile(lib):
    os.system("pwd")
    opts = lib['opts']
    
    # Run configure and make install
    os.system("./configure %s && sudo make && sudo make install" % opts)
    
    
# Clone/download all repos
def get_git_repos():
    for lib in libraries:
        repo = lib['repo']
        folder = lib['folder']
        
        print "REPO: %s" % folder
        os.system("git clone %s %s/%s" % (repo, top_dir, folder))
    
    
# Compile libraries
def compile_libs():
    for lib in libraries:
        folder = lib['folder']
        
        # cd into directory
        os.chdir("%s/%s" % (top_dir, folder))
        
        if os.path.exists("configure"):
            print '"configure" exists: %s' % folder
            run_compile(lib)
            
        elif os.path.exists("configure.ac"):
            print '"configure.ac" exists: %s' % folder
            os.system("autoreconf -is")
            run_compile(lib)
            
        else:
            print "configure does not exist for %s" % folder
            
# Step 1: Clone the repos
get_git_repos()

# Step 2: Compile the libraries
compile_libs()
