import re
import sys
from os.path import exists
from setuptools import find_packages, setup
version_file = 'mtl/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


def parse_requirements(fname='requirements.txt', with_version=True):

    require_fpath = fname

    def parse_line(line):
        """Parse information from a line in a requirements text file."""
        if line.startswith('-r '):
            # Allow specifying requirements in other files
            target = line.split(' ')[1]
            for info in parse_require_file(target):
                yield info
        else:
            info = {'line': line}
            if line.startswith('-e '):
                info['package'] = line.split('#egg=')[1]
            else:
                # Remove versioning from the package
                pat = '(' + '|'.join(['>=', '==', '>']) + ')'
                parts = re.split(pat, line, maxsplit=1)
                parts = [p.strip() for p in parts]

                info['package'] = parts[0]
                if len(parts) > 1:
                    op, rest = parts[1:]
                    if ';' in rest:
                        version, platform_deps = map(str.strip, rest.split(';'))
                        info['platform_deps'] = platform_deps
                    else:
                        version = rest  # NOQA
                    info['version'] = (op, version)
            yield info

    def parse_require_file(fpath):
        with open(fpath, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    for info in parse_line(line):
                        yield info

    def gen_packages_items():
        if exists(require_fpath):
            for info in parse_require_file(require_fpath):
                parts = [info['package']]
                if with_version and 'version' in info:
                    parts.extend(info['version'])
                platform_deps = info.get('platform_deps')
                if platform_deps is not None:
                    parts.append(';' + platform_deps)
                item = ''.join(parts)
                yield item

    packages = list(gen_packages_items())
    return packages


if __name__ == '__main__':
    setup(
        name='multitask',
        version=get_version(),
        description='MultiTask Training Library',
        long_description='',
        long_description_content_type='',
        author='Andy',
        keywords='AI',
        url='',
        packages=find_packages(exclude=('tools', 'data', 'checkpoint', 'work_dirs')),
        include_package_data=True,
        classifiers=[
            'Development Status :: 1 - Planning',
            # 'Development Status :: 2 - Pre-Alpha',
            # 'Development Status :: 3 - Alpha',
            # 'Development Status :: 4 - Beta',
            # 'Development Status :: 5 - Production/Stable',
            # 'Development Status :: 6 - Mature',
            # 'Development Status :: 7 - Inactive',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.x',
            'Topic :: Scientific/Engineering :: Artificial Intelligence'
        ],
        license='Apache License 2.0',
        install_requires=parse_requirements('requirements.txt'),
        extras_require={},
        ext_modules=[],
        zip_safe=False)
