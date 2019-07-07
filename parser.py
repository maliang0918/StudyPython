import argparse
parser = argparse.ArgumentParser()
parser.description='Give me two number, we will give the mutiply.'
parser.add_argument("-a","--ParA", help="I am A",type=int)
parser.add_argument("-b","--ParB", help="I am B",type=int)
args = parser.parse_args()
if args.ParA:
    print("A is ",args.ParA)
if args.ParB:
    print("B is ",args.ParB)
if args.ParA and args.ParB:
    print("A mutiply B is ",args.ParA*args.ParB)
