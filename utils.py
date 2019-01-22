def is_chinese(str):
  for s in str:
    if u'\u4e00' <= s <= u'\u9fff':
      return True