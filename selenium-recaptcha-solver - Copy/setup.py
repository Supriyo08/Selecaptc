from setuptools import setup, find_packages


setup(
    name='selenium-recaptcha-solver',
    version='1.9.0',
    license='MIT',
    author='supriyo maji',
    author_email='akashmaji200680@gmail.com',
    packages=find_packages(exclude=('tests*', 'testing*')),
    url='',
    download_url='',
    keywords='python, captcha, speech recognition, selenium, web automation',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'selenium~=4.8.0',
        'pydub~=0.25.1',
        'SpeechRecognition~=3.8.1',
        'requests>=2.28.1,<2.33.0',
    ],
)
