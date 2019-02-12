import sortedcontainers
import collections

Point = collections.namedtuple('Point', 'x y')


def parse_in(in_file):
    with open(in_file, 'r') as f:
        pass


def parse_ans(ans_file):
    with open(ans_file, 'r') as f:
        pass


def write_ans(in_file, answer):
    """
    Takes an in_file and generates an appropriate outfile.
    Return the path to outfile.
    """
    problem_name = in_file.split('/')[-1].replace('.in', '.ans')
    outfile = 'out/{}'.format(problem_name)

    print('Writing {} -> {}'.format(in_file, outfile))
    with open(outfile, 'w') as f:
        pass
