[app]
title = RandomPicker
package.name = randompicker
package.domain = org.example
source.dir = .
source.include_exts = py
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET
android.archs = arm64-v8a
version = 1.0.0  
[buildozer]
log_level = 2
warn_on_root = 1
android.debug_build = False      # 原来是 True
android.ndk = 25b            # ≥24 即可，越小越好
android.build_tools = 36.0.0
android.api = 34
android.add_aars =
android.blacklist_src = blacklist.txt