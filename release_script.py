import os
import shutil
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-dir', help='Source folder')
    parser.add_argument('-r', '--release-dir', help='Release folder')
    parser.add_argument('-v', '--releaes-version', help='Release version')
    args = parser.parse_args()
    if os.path.isdir(args.release_dir):
        shutil.rmtree(args.release_dir)
    os.mkdir(args.release_dir)
    for cur_dir, dirs, files in os.walk(args.source_dir):
        rel_path = os.path.relpath(cur_dir, args.source_dir)
        for dir_ in dirs:
            os.mkdir(os.path.join(args.release_dir, rel_path, dir_))
        for file_ in files:
            shutil.copy(os.path.join(cur_dir, file_), os.path.join(args.release_dir, rel_path, file_))
    subprocess.check_call(['git', 'commit', '-m{0}'.format(args.release_version)])
    subprocess.check_call(['git', 'push'])


if __name__ == '__main__':
    main()
