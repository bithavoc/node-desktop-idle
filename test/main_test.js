var vows = require('vows');
var assert = require('assert');
var desktopIdle = require('../');
vows.describe('getIdleTime()').addBatch({
  'return value': () => {
    var idle = desktopIdle.getIdleTime()  
    console.log("test idle", idle);
    assert.ok(idle > 0, 'should return idle time');
  }
}).run();