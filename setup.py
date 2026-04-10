from setuptools import setup, find_packages


def get_requirements(file_path: str) -> list[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="xry",
    version="0.0.1",
    author="Darshit",
    author_email="darshit.1066@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
