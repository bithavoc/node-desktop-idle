#include "../idle.h"
#include <X11/extensions/scrnsaver.h>

double desktop_idle_get_time() {
  Display *dpy = XOpenDisplay(NULL);
  if (!dpy) {
    return(1);
  }
  XScreenSaverInfo *info = XScreenSaverAllocInfo();
  XScreenSaverQueryInfo(dpy, DefaultRootWindow(dpy), info);
  unsigned long idle = info->idle;
  XFree(info);
  XCloseDisplay(dpy);
  return idle / 1000.0; // to seconds
}