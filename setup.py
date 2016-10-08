from setuptools import setup, find_packages


setup(
    name='pretix-quota-burndown',
    version='0.0.1',
    description='Quota burndown charts',
    long_description='Shows a burndown chart for quotas and tries a prediction for quota availability',
    author='Tobias Kunze',
    author_email='rixx@cutebit.de',

    include_package_data=True,
    entry_points="""
[pretix.plugin]
quotaburndown=quota_burndown:PretixPluginMeta
""",
)
