from setuptools import setup, find_packages

setup(
    name="converter_letra_numero",         # nome do pacote
    version="0.1.0",                       # versão inicial
    description="Converte letras (A–Z) em índices numéricos (0–25)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    url="https://github.com/seuusuario/converter_letra_numero",  # link do repositório
    license="MIT",
    packages=find_packages(exclude=["tests*", "docs*"]),
    install_requires=[
        # nenhuma dependência externa
    ],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

