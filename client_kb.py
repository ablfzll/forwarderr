from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def mainmenu():
	ikb = InlineKeyboardMarkup()
	ikb.add(InlineKeyboardButton(text='📈 all photos', callback_data='allphotos'))
	ikb.add(InlineKeyboardButton(text='📈 all videos', callback_data='allvidos'))
	ikb.add(InlineKeyboardButton(text='📈 change caption', callback_data='caption'))
	return ikb

def editCaption():
	ikb = InlineKeyboardMarkup()
	ikb.add(InlineKeyboardButton(text='Edit Caption', callback_data='editCaption'))
	return ikb