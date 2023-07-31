var FORM_ID = 'GoogleformID'; 
var TOKEN = 'BotTelegramToken'; 
var CHAT_ID = 'TelegramChatID/Groups'; 

function formSubmitTrigger(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Form Responses 1');
  var range = sheet.getRange(sheet.getLastRow(), 1, 1, sheet.getLastColumn());
  var values = range.getValues()[0];

  var message = 'Some one has Input Form:\n';

  for (var i = 0; i < values.length; i++) {
    var question = sheet.getRange(1, i + 1).getValue();
    var answer = values[i];
    message += question + ': ' + answer + '\n';
  }

  sendToTelegram(message);
}

function sendToTelegram(text) {
  var url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage';
  var payload = {
    method: 'post',
    payload: {
      chat_id: CHAT_ID,
      text: text,
      parse_mode: 'HTML'
    }
  };

  UrlFetchApp.fetch(url, payload);
}