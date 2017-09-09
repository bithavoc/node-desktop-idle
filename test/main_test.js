var test = require('tape');
var desktopIdle = require('../');

test('getIdleTime()', (assert) => {
  var idle = desktopIdle.getIdleTime()
  assert.ok(idle > 0, 'should return idle time');
  assert.end();
});