import os
import shutil
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-dir', help='Source folder')
    parser.add_argument('-r', '--release-dir', help='Release folder')
    parser.add_argument('-v', '--release-version', help='Release version')
    args = parser.parse_args()
    if os.path.isdir(args.release_dir):
        shutil.rmtree(args.release_dir)
    shutil.copytree(args.source_dir, args.release_dir)
    subprocess.check_call(['git', 'commit', '-m{0}'.format(args.release_version)])
    subprocess.check_call(['git', 'push'])


if __name__ == '__main__':
    main()
