"""
 versão Maior(MAJOR): quando fizer mudanças incompatíveis na API,
 versão Menor(MINOR): quando adicionar funcionalidades mantendo compatibilidade, e
 versão de Correção(PATCH): quando corrigir falhas mantendo compatibilidade.
 """

from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]


setup(
    name="delivery",
    version="0.1.0",
    description="Delivery app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)
