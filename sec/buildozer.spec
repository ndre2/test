[app]

# Application title
title = Helper - Home Monitoring

# Package name (no spaces, lowercase)
package.name = helper

# Package domain
package.domain = org.helper.monitor

# Source directory
source.dir = .

# Source includes patterns
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Requirements
requirements = python3,kivy,android

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 1

# Android-specific
android.permissions = INTERNET,RECORD_AUDIO
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Build configuration
[buildozer]

# Log level
log_level = 2

# Display warning upon run
warn_on_root = 1
