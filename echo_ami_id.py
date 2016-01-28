import click
import sys

@click.command()
@click.option('--ami_id', '-i',
              help='the AMI ID to echo',
              type=str)
def echo_ami_id(ami_id):
    exit_status = True
    if ami_id is not None:
        print "AMI id passed to this script: {}".format(ami_id)
    else:
        print "No AMI id passed to the script!"
        exit_status = False

    sys.exit(not exit_status)

if __name__ == '__main__':
    echo_ami_id()