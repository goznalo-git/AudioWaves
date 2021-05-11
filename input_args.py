def initiation():
    '''This function initiates the script, retrieving the necessary arguments and options'''
    
    import argparse

    parser = argparse.ArgumentParser(description='Generate static or dynamical visualizations of audio waves and their spectrums')

    parser.add_argument('file')
    parser.add_argument('-s', '--static', action='store_true', default=False, help='Use this option to generate a png image of the full audio clip rather than a gif.') 
    parser.add_argument('-c', '--chunk', default=10, type=int, help='Use this option to specify the length of each cut used for the animation.') 
    parser.add_argument('-l', '--linewidth', default=0.3, type=float, help = 'Line width parameter for the plot.') 

    subparsers = parser.add_subparsers(dest='mode', help='Available sub-commands')

    subparser_a = subparsers.add_parser('audio', help='audio sub-command help')
    subparser_s = subparsers.add_parser('spectrum', help='spectrum sub-command help')
    #subparser.add_argument('-m', '--mode', choices=['audio','spectrum'], default='audio') # choose between audio and spectrum 

    subparser_s.add_argument('-p', '--periodogram', choices=['simple','log','sqrt','Welch','Daniell','Corr'], default='simple', help="Choice of spectrum type")
    subparser_s.add_argument('-L','--lag', default=100, type=int, help="Parameter for the Welch periodogram")
    subparser_s.add_argument('-P','--points', default=8, type=int, help="Parameter for the Daniell periodogram")

    args = vars(parser.parse_args())
    
    return args
    
   