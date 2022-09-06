import argparse
import sys


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    print(f"Now I need to process the records in {args.fasta}")
    print(f"and the coordinates in {args.coords}")


    for line in args.coords:
        #Initilize
        seq = ''
        found = False

        coord_list = line.split()
        #Reset args.fasta to line 0
        args.fasta.seek(0)

        for line2 in args.fasta:
            #If header found
            if coord_list[0] in line2:
                found = True 
            #Append sequence as long as header found but new Seq didn't start
            elif found == True and (line2.startswith('>') == False):
                seq = "".join((seq, line2))
            #Break when new Seq starts
            elif found == True and (line2.startswith('>')):
                break
            
        #Print Subsequence
        print(seq[int(coord_list[1])-1:int(coord_list[2])-1])
    print()
    args.fasta.close()
    args.coords.close()   

if __name__ == '__main__':
    main()
