#!/usr/bin/env python
# _*_ coding: utf8 _*_

import os
import imp

urls = []

# 扫描urls目录下的所有的urls必须为list
for parent, dir_path, file in os.walk(os.path.dirname(__file__)):
    for item in file:
        if item == "__init__.py" or item.endswith(".pyc"): continue
        module = imp.load_source(item.split(".")[0], os.path.join(parent, item))
        if hasattr(module, "urls"):
            if not isinstance(module.urls, list): continue
            urls += module.urls

GLOBAL_URLS = urls
