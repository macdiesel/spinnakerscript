import click

@click.command()
@click.option('--ami_id', '-i',
              help='the AMI ID to echo',
              type=str)
def echo_ami_id(ami_id):
    print "AMI id passed to this script: %s".format(ami_id)