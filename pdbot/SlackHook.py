import os
import time
from slackclient import SlackClient
from profiler_logging import profiler_logging
from profiler_logging import LOG as logger
from CommandParser import CommandParser


class SlackHook:

    LISTENING = True
    
    @profiler_logging
    def __init__(self):
        self._token = os.environ.get("BOT_SLACK_TOKEN") or "xoxb-295087394756-oEA3psh25Mu1EpbdJTinwMUI"
        self._slack_client = SlackClient(self._token)
        self._getBotId()
        self._at_bot = "<@" + self._bot_id + ">"
        self._command_parser = CommandParser()
        
    @profiler_logging
    def _getBotId(self):
        response = self._slack_client.api_call('users.list')
        if response.get('ok'):
            _members = response.get('members')
            for _m in _members:
                if _m['name'] == self._bot_name:
                    self._bot_id = _m.get('id')
                    
    @profiler_logging
    def get_slack_client(self):
        return self._slack_client
    
    @profiler_logging
    def listen(self):
        _websocket_delay = 1
        if self._slack_client.rtm_connect():
            logger.info("pdbot connected, and running!")
            while SlackHook.LISTENING:
                command, channel, user = self._parse_slack_output(self._slack_client.rtm_read())
                if command and channel:
                    self._handle_command(command, channel, user)
                time.sleep(_websocket_delay)
        else:
            logger.error("Connection failed. Token and bot ID okay?")
            
    @profiler_logging
    def _parse_slack_output(self, rtm_output):
        if len(rtm_output) != 0:
            logger.debug(rtm_output)
        if rtm_output and len(rtm_output) > 0:
            for output in rtm_output:
                if "user" in output.keys():
                    if output['type'] == "message" and output['user'] != self._bot_id:
                        return output['text'], output['channel'], output['user']
        return None, None, None
    
    @profiler_logging
    def _handle_command(self, command, channel, user):
        logger.info("command was {0}, channel was {1}".format(command, channel))
        command_output = self._command_parser.parse_command(command)
        if command_output:
            response = ("<@{0}> ".format(user)) + command_output
            self._slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

    @profiler_logging
    def shutdown(self):
        SlackHook.LISTENING = False


def main():
    sh = SlackHook()
    sh.listen()

if __name__ == "__main__":
    main()
