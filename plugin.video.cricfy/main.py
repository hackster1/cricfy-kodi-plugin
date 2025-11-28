import sys
import xbmcgui

# Base URL for the addon
BASE_URL = sys.argv[0]
ADDON_HANDLE = int(sys.argv[1])


def router(param_string):
  xbmcgui.Dialog().notification(
      'Error', 'Not yet implemented', xbmcgui.NOTIFICATION_ERROR)


if __name__ == '__main__':
  router(sys.argv[2][1:])
