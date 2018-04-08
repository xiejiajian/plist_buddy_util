# plist_buddy_util
A python3 version of encapsulation of PlistBuddy.

## How to use

### import PlistBuddy ###

    from plist_buddy_util import PlistBuddy
    pb = PlistBuddy("myXcodeProject/info.plist")

### set 'CFBundleVersion' to '1.0.0' ###

    pb.set_value('CFBundleVersion', '1.0.0')

### get value of 'CFBundleShortVersionString' ###

    pb.get_value('CFBundleShortVersionString')
