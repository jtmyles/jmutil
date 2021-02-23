import os
import datetime

def upload_to_dropbox(outfile, hostname='slac', repo_dir='/u/ki/jmyles/repositories/'):
    command = '{0}Dropbox-Uploader/dropbox_uploader.sh upload {1} {2}/{3}/{4}'
    os.system(command.format(repo_dir,
                             outfile,
                             str(datetime.datetime.today())[:10],
                             hostname,
                             outfile.split('/')[-1]))
    return

def save_figure(fig, outfile, png=True, svg=False, pdf=False, dropbox=False, **kwargs):
    if svg:
        print('write ' + outfile + '.svg')
        fig.savefig(outfile + '.svg')
    if png:
        print('write ' + outfile + '.png')
        fig.savefig(outfile + '.png', dpi=150)
        if dropbox:
            upload_to_dropbox(outfile + '.png', **kwargs)
    if pdf:
        print('write ' + outfile + '.pdf')
        fig.savefig(outfile + '.pdf')
