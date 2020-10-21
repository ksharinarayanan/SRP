## greet and ask name
* greet
  - utter_greet
* tell_name{"user_name": "john"}
  - utter_acknowledge_name
* thanks
  - utter_goodbye

## ask name to the bot
* ask_name
  - action_utter_name

## greet and tell company name
* greet
  - utter_greet
* tell_company{"company": "google"}
  - action_acknowledge_company
* tell_no_of_days_later{"days_later": "1"}
  - action_predict_price

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
