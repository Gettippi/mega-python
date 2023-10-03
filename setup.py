import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
 #   long_description = fh.read()
with open("requirements", "r", encoding="utf-8") as fh:
    req = fh.read()

setuptools.setup(
    name='mega-python',
    version='0.0.1',
    author='Gettippi',
    author_email='jade.ai@pm.me',
    description='Stuff regularly used',
    long_description="",
    long_description_content_type="text/markdown",
    url='https://github.com/Gettippi/mega-python',
    project_urls = {
        "Bug Tracker": "https://github.com/Gettippi/mega-python/issues"
    },
    license='MIT',
    packages=['mega-python'],
    install_requires= req,
)