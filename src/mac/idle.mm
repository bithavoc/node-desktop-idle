#include "../idle.h"
#import <CoreFoundation/CoreFoundation.h>
#import <AppKit/AppKit.h>

double desktop_idle_get_time() {
  return CGEventSourceSecondsSinceLastEventType(kCGEventSourceStateHIDSystemState, kCGAnyInputEventType);
}