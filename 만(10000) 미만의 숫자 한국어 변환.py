#!/usr/bin/env python
# coding: utf-8

# In[41]:


def Num2Korean(n):
    if n <= 0 or n >= 10000:
        return "입력한 숫자가 10000을 초과했습니다"
  
    units = [''] + list('십백천')
    nums = '일이삼사오육칠팔구'
    result = []
    i = 0
    while n > 0:
        n, r = divmod(n, 10)
        if r > 0:
            result.append(nums[r-1] + units[i])
        i += 1
    korean=''.join(result[::-1])
    korean = korean.replace('일십', '십').replace('일백', '백').replace('일천', '천')
    return korean


# In[40]:


print(Num2Korean(10000))


# In[42]:


print(Num2Korean(9999))


# In[43]:


print(Num2Korean(1111))


# In[44]:


print(Num2Korean(1010))

