from telebot import types


def get_start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept_conditions = types.InlineKeyboardButton('Accept terms and conditions', callback_data='accept_conditions')
    markup.add(accept_conditions)
    return markup


def get_main_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    see_menu = types.InlineKeyboardButton('Cake menu', callback_data='see_cake_menu')
    custom_cake = types.InlineKeyboardButton('Custom cake', callback_data='custom_cake_about')
    see_last_order_delivery_status = types.InlineKeyboardButton('Check delivery status', callback_data='last_order_delivery_status')
    see_history = types.InlineKeyboardButton('Order history', callback_data='see_history')
    markup.add(see_menu, custom_cake, see_last_order_delivery_status, see_history)
    return markup


def get_cake_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    position_1 = types.InlineKeyboardButton('1', callback_data='cake_menu_position_1')
    position_2 = types.InlineKeyboardButton('2', callback_data='cake_menu_position_2')
    position_3 = types.InlineKeyboardButton('3', callback_data='cake_menu_position_3')
    position_4 = types.InlineKeyboardButton('4', callback_data='cake_menu_position_4')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(position_1, position_2, position_3, position_4, back_to_main)
    return markup


def get_custom_cake_about_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept = types.InlineKeyboardButton('Order a custom cake', callback_data='custom_cake_start')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(accept, back_to_main)
    return markup


def get_custom_cake_inscription_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    add_inscription = types.InlineKeyboardButton('Add', callback_data='add_inscription')
    no_inscription = types.InlineKeyboardButton('Dont add', callback_data='no_inscription')
    back_to_custom_cake_decorations = types.InlineKeyboardButton('Back', callback_data='back_to_previous_state')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    markup.add(add_inscription, no_inscription, back_to_custom_cake_decorations, back_to_main)
    return markup


def get_writing_custom_cake_inscription_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    cancel_inscription = types.InlineKeyboardButton('Cancel', callback_data='cancel_inscription')
    markup.add(cancel_inscription)
    return markup


def get_last_order_delivery_status_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(back_to_main)
    return markup
    

def get_history_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    repeat_last_order = types.InlineKeyboardButton('Repeat last order', callback_data='repeat_last_order')
    repeat_select_order = types.InlineKeyboardButton('Repeat specific order', callback_data='repeat_specific_order')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(repeat_last_order, repeat_select_order, back_to_main)
    return markup

def get_repeat_last_order_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept_repeat_last_order = types.InlineKeyboardButton('Do you wish to repeat this order ?', callback_data='accept_repeat_last_order')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(accept_repeat_last_order, back_to_main)
    return markup

def get_inscription_confirm_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirm = types.InlineKeyboardButton('Inscription is correct', callback_data='confirm_iscription')
    cancel = types.InlineKeyboardButton('Reenter inscription', callback_data='reenter_inscription')
    markup.add(confirm, cancel)
    return markup

def get_address_confirm_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirm = types.InlineKeyboardButton('Address is correct', callback_data='confirm_address')
    reenter = types.InlineKeyboardButton('Reenter address', callback_data='reenter_address')
    markup.add(confirm, reenter)
    return markup

def get_receiver_confirm_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirm = types.InlineKeyboardButton('Receivers name is correct', callback_data='confirm_receiver')
    reenter = types.InlineKeyboardButton('Reenter name', callback_data='reenter_receiver')
    markup.add(confirm, reenter)
    return markup

def get_comment_confirm_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirm = types.InlineKeyboardButton('Comment is correct', callback_data='confirm_comment')
    reenter = types.InlineKeyboardButton('Reenter comment', callback_data='reenter_comment')
    markup.add(confirm, reenter)
    return markup

def get_order_finish_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(back_to_main)
    return markup

def get_urgent_confirm_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirm = types.InlineKeyboardButton('Fast delivery', callback_data='confirm_urgent')
    decline = types.InlineKeyboardButton('Normal delivery', callback_data='not_urgent')
    markup.add(confirm, decline)
    return markup


def get_menu_cake_confirm_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirm = types.InlineKeyboardButton('Order this cake', callback_data='confirm_order_menu_cake')
    decline = types.InlineKeyboardButton('Cancel', callback_data='decline_order_menu_cake')
    markup.add(confirm, decline)
    return markup