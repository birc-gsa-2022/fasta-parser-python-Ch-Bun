import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    #print(f"Now I need to process the records in {args.fasta}")
    Printer = ''
    Seq_to_Print = False 
    for line in args.fasta:

            if line.startswith('>'):
                if Seq_to_Print == True:
                    print(Printer)
                    Printer = ''
                    Seq_to_Print = False
                Printer = "".join((Printer, line[1:len(line)].strip(), "\t"))
                Seq_to_Print = True
            else:
                Printer = "".join((Printer, line.strip()))
    #Print last line
    print(Printer)
 
if __name__ == '__main__':
    main()
