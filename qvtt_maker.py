from optparse import OptionParser
import urllib2


def main():
    optp = OptionParser()
    #settings
    optp.add_option('-u', '--url', help='url of the media file on Qiniu',
                    dest='url', default=None)
    optp.add_option('-o', '--output', help='output file name',
                    dest='output', default='sample.vtt')

    opts, args = optp.parse_args()

    if not opts.url:
        print 'need a url'
        return




if __name__ == '__main__':
    main()