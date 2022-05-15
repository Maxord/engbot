
import telebot
from file_of_text import *
import time
import random
class Bot():
    def __init__(self):
        self.bot = telebot.TeleBot('5340919234:AAGk24VPKHYHtXjuydBxhQ8oDjt5NqxeCtM')
        self.choice=telebot.types.InlineKeyboardMarkup([
            [
                telebot.types.InlineKeyboardButton(text='Test',item_name='test',callback_data='test')

            ],
            [
                telebot.types.InlineKeyboardButton(text='Info about', item_name='Info', callback_data='Info')
            ]
        ])
        self.keyboard_main = telebot.types.ReplyKeyboardMarkup(False)
        self.keyboard_main.add('Времена', 'Артикли', 'Conditional','Information about us')
        self.keyboard_category = telebot.types.ReplyKeyboardMarkup(False)
        self.keyboard_category.add('PastSimple')
        self.keyboard_Present_Simple = telebot.types.ReplyKeyboardMarkup(True)
        self.keyboard_Present_Simple.add('Module1', 'Module2', 'Module3', 'Module4', 'Module5', 'Return to categories')
        self.tests = 0
        self.category=0
        self.mark=0
        self.time_h_m_s_d_m_y = lambda x: time.strftime("%Hh%Mm%Ss %d.%m.%Y", time.localtime(x))
        self.time_minutes_seconds = lambda x: time.strftime("%M(m):%S(s)", time.localtime(x))
        self.fail = []
        self.rating = 620
        self.name_of_test = None
        self.programm()


    def programm(self):

        
        @self.bot.message_handler(commands=["start"])
        def send_help(message):
            self.bot.send_message(message.chat.id, text="Welcome text here")

        @self.bot.message_handler(commands=["help"])
        def send_help(message):
            self.bot.send_message(message.chat.id, text="Help text here")

        @self.bot.message_handler(commands=["rating"])
        def send_help(message):
            self.bot.send_message(message.chat.id, text=f"You have {self.rating} mmr")


##################################################################################################################

###                                               Test part                                                    ###

##################################################################################################################

        @self.bot.message_handler(commands=["engtest"])
        def category(message):
            self.bot.send_message(message.chat.id,text='Please choose category',reply_markup=self.keyboard_category)





        @self.bot.message_handler(content_types=["text"])


        def change_category(message):


            def test(message):

                self.keyboard_test_1 = telebot.types.ReplyKeyboardMarkup(True)
                self.keyboard_test_1.row(Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests][0],
                                         Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests][1],
                                         Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests][2])
                self.bot.send_message(message.chat.id,
                                      f"{self.tests}.{Past_Simple_All_Questions_and_Answers[self.name_of_test][0][self.tests]}",
                                      reply_markup=self.keyboard_test_1)
                self.tests = self.tests + 1
            if message.text in Name_of_main:
                self.bot.send_message(message.chat.id, 'Choose category:', reply_markup=self.keyboard_category)
            if message.text in Name_of_categories:
                self.bot.send_message(message.chat.id, 'Choose module:', reply_markup=self.keyboard_Present_Simple)

            if message.text=='Return to categories':
                category(message)


            if message.text==message.text:
                if message.text in Name_of_modules:
                    self.name_of_test = message.text
                    self.timer_start = message.date
                    test(message)
                if self.name_of_test in Name_of_modules:


                    if message.text == Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests - 1][3]:
                        tests= len(Past_Simple_All_Questions_and_Answers[self.name_of_test][0])
                        self.mark = self.mark + 1
                        self.bot.send_message(message.chat.id, random.choice(Congratulations),
                                              reply_markup=telebot.types.ReplyKeyboardRemove(True))

                        if self.tests == tests:
                            self.tests = 0

                            self.timer_end = message.date
                            self.bot.send_message(message.chat.id,
                                                  f'{self.name_of_test}\nYou have {self.mark * 10} marks\nSuccesfull: {self.mark} Wrong answers: {len(Past_Simple_All_Questions_and_Answers[self.name_of_test][0]) - self.mark}\nTime, which you spend {self.time_minutes_seconds(self.timer_end - self.timer_start)}')
                            joinedFile = open("tests.txt", 'a')
                            joinedFile.write(str(message.from_user.first_name) + '==>' + self.time_h_m_s_d_m_y(
                                message.date) + '  ' + f'{self.fail}' + '\n')
                            joinedFile.close()
                            self.mark = 0
                            category(message)
                        else:
                            test(message)

                    elif message.text != Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests - 1][3]:
                        tests = len(Past_Simple_All_Questions_and_Answers[self.name_of_test][0])
                        if message.text == Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests - 1][2] or message.text ==Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests - 1][1] or message.text == Past_Simple_All_Questions_and_Answers[self.name_of_test][1][self.tests - 1][0]:
                            self.fail.append(f"For question {self.tests} {Past_Simple_All_Questions_and_Answers[self.name_of_test][0][self.tests - 1]}  "'Answer is : ' + str(
                                    message.text))
                            self.bot.send_message(message.chat.id, random.choice(Fails),
                                                  reply_markup=telebot.types.ReplyKeyboardRemove(True))

                            if self.tests == tests:
                                self.tests = 0

                                self.timer_end = message.date
                                self.bot.send_message(message.chat.id,f'{self.name_of_test}\nYou have {self.mark * 10} marks\nSuccesfull: {self.mark} Wrong answers: {len(Past_Simple_All_Questions_and_Answers[self.name_of_test][0]) - self.mark}\nTime, which you spend {self.time_minutes_seconds(self.timer_end - self.timer_start)}')
                                joinedFile = open("tests.txt", 'a')
                                joinedFile.write(str(message.from_user.first_name) + '==>' + self.time_h_m_s_d_m_y(message.date) + '  ' + f'{self.fail}' + '\n')
                                joinedFile.close()
                                self.mark = 0
                                category(message)
                            else:
                                test(message)




##################################################################################################################

###                                              End of test part                                              ###

##################################################################################################################





        self.bot.polling(none_stop=True)




if __name__ == "__main__":
    app = Bot()