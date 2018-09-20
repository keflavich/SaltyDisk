import os
import tarfile
import shutil

if os.path.exists('apj_tar'):
    shutil.rmtree('apj_tar')
os.mkdir('apj_tar')

with open('saltydisk.tex','r') as fhr:
    with open('saltydisk_apjform.tex', 'w') as fhw:
        for line in fhr:
            if 'figures/' in line:
                fhw.write(line.replace("figures/",""))
                fn = line.split("figures/")[-1].replace("{","").replace("}","").strip()
                print(fn)
                if not os.path.exists('apj_tar/{0}'.format(fn)):
                    os.link('figures/{0}'.format(fn), 'apj_tar/{0}'.format(fn))
            else:
                fhw.write(line)


critical_files = [
    'apjmacros.tex',
    'authors.tex',
    'gitstuff.tex',
    'macros.tex',
    'preface.tex',
    'solobib.tex',
    'saltydisk_apjform.tex',
    'extracted.bib',
    'saltydisk.bbl',
]

for fn in critical_files:
    if not os.path.exists('apj_tar/{0}'.format(fn)):
        os.link(fn, 'apj_tar/{0}'.format(fn))

with tarfile.open('apj.tgz', mode='w:gz') as tf:
    tf.add('apj_tar')
