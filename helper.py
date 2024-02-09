import re

def extract_internalmemory(string):
    return string

def extract_os_versions(string):
    # Define the regex pattern to match OS versions

    pattern = r'(?P<lower>(?P<os>(Android|iOS))\s+(\d+(\.\d+)?))(?:,\s*up\s+to\s+(?P<upper>(Android|iOS)\s+(\d+(\.\d+)?))?)?'
    
    # Use regex to find matches
    matches = re.search(pattern, string)
    
    if matches:
        lower_version = matches.group('lower')
        upper_version = matches.group('upper')
        return lower_version, upper_version
    else:
        return None, None


def test_extract_os_versions():
    tests = [
        "Android 13, up to Android 14",
        "Android 13", 
        "iOS 15, up to iOS 17",
        "iOS 17"
        ]

    for s in tests:
        print(s)
        print(extract_os_versions(s))
        print('done')