import platform
import subprocess
import sys

# should this account for virtual enviroments?

# i also am on a mac, and cant test windows 11 this moment, so some of this may be off.

# can we use case statements added in 3.10? 
# it would hinder compatiblity, but would remove having to check for recent python.
# also, check_python_version only checks for major, not minor.
def check_platform(): # not needed currenty, but there for when it is.
    if platform.system() == 'Windows':
        return 'Windows'
    elif platform.system() == 'Linux':
        return 'Linux'
    elif platform.system() == 'Darwin':
        return 'Mac'
    else:
        return 'Unknown Platform'

def check_java_version():
    # should we be looking for the path or just use env varible?
    try:
        output = subprocess.check_output(['java', '--version'], text=True, stderr=subprocess.STDOUT) 
        
        # eat 1st line, split to words, and get 2nd word, then convert to string
        version = output.split('\n')[0].split()[1]

        # split version into a list at each '.'
        version_parts = list(map(int, version.split('.'))) 

        if version_parts[0] >= 21: # do we need exactly 21?
            return True
        else:
            raise Exception("Insufficent java version. Java >= 21 required.")
    except:
        raise Exception("'java' not found in env varibles")

def check_python_version():
    major_version =  sys.version_info[0]

    if major_version >= 3:
        return True
    else:
        raise Exception("Python 3 required!")

def check_maven_installed():
    try:
        output = subprocess.check_output(['mvn', '-v'], text=True, stderr=subprocess.STDOUT) # its done with a var so we can check its the right maven
    except:
        raise Exception("Maven not found.")

def check_docker():
    try:
        subprocess.check_output(['docker', '-v'])
        return True
    except:
        raise Exception("Docker not found.")
    
def check_docker_compose():
    try:
        subprocess.check_output(['docker-compose', '-v'])
        return True
    except:
        raise Exception("Docker Compose not found.")

def pull_sample_container(): # should this be optional? some people have data limits.
    print("pulling sample container...")
    try:
        subprocess.check_output(['docker', 'pull', 'hello-world'], text=True, stderr=subprocess.STDOUT)
        return True
    except Exception as e:
        raise Exception("Failed to pull Docker container: " + str(e) + " is docker running?")

def main():
    # check platform
    platform = check_platform()

    print(f"Platform: {platform}")

    check_java_version()
    check_python_version()
    check_maven_installed()
    check_docker()
    check_docker_compose()

    pull_sample_container()


if __name__ == "__main__":
    main()