#include <node.h>
#include "idle.h"

namespace desktopIdle {

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Object;
using v8::Number;
using v8::Value;

void desktopIdleGetIdleTime(const FunctionCallbackInfo<Value>& args) {
  Isolate* isolate = args.GetIsolate();
  double idleSeconds = desktop_idle_get_time();
  args.GetReturnValue().Set(Number::New(isolate, static_cast<double>(idleSeconds)));
}

void init(Local<Object> exports) {
  NODE_SET_METHOD(exports, "getIdleTime", desktopIdleGetIdleTime);
}

NODE_MODULE(desktopIdle, init)

}  // na