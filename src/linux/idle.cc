#include "../idle.h"
#include <X11/extensions/scrnsaver.h>

double desktop_idle_get_time() {
  Display *dpy = XOpenDisplay(NULL);
  if (!dpy) {
    return(1);
  }
  XScreenSaverInfo *info = XScreenSaverAllocInfo();
  XScreenSaverQueryInfo(dpy, DefaultRootWindow(dpy), info);
  return info->idle / 1000; // to seconds
}