pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'riddles')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'riddles.in',
           output: 'riddles',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir')
)

riddles_sources = [
    '__init__.py',
    'main.py'
]

install_data(riddles_sources, install_dir: moduledir)
