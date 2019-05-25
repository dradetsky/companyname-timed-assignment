const fs = require('fs')
const hapi = require('@hapi/hapi')
const moment = require('moment')
const promisify = require('util').promisify

const appendFile = promisify(fs.appendFile)

const logfile = 'events.txt'

async function logEvent(req, res) {
  const event = req.payload
  event.datetime = moment()
  await appendFile(logfile, JSON.stringify(event) + "|")
  return 'ok'
}

async function start() {
  const srv = hapi.server({
    host: 'localhost',
    port: 3000,
  })

  srv.route({
    method: 'POST',
    path: '/delivery',
    handler: logEvent
  })

  await srv.start()
  console.log('running on %s', srv.info.uri)
}

start()
