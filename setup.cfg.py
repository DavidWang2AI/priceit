[metadata]
name = priceit
version = 0.1.1
author = David Wang
author_email = davidwang.2ai@gmail.com
description = Data extractor in financial market, including realtime price, history price, financial statements and more. Besides stocks, cryptocurrency is also covered.
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/DavidWang2AI/priceit
project_urls =
    Bug Tracker = https://github.com/DavidWang2AI/priceit/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src