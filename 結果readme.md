gemini_1.5_flash_output和gemini_2.5_pro_output 執行OCR測試結果






1. 

[第1張圖](input/1.png)
gemini_1.5_flash <font color="red">**錯1字**</font>
O:今天天氣很好，我們下午去公園散步。 <font color="blue">**正確**</font>
O:請在下午3點前，到A棟201號會議室開會。
X:請在下午3點前，到<font color="red">**日**</font>棟201號會議室開會。
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。 <font color="blue">**正確**</font>
O:你真的相信「天下沒有白吃的午餐」這句話嗎？ <font color="blue">**正確**</font>

gemini_2.5_pro <font color="blue">**全對**</font>
O:今天天氣很好，我們下午去公園散步。 <font color="blue">**正確**</font>
O:請在下午3點前，到A棟201號會議室開會。 <font color="blue">**正確**</font>
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。 <font color="blue">**正確**</font>
O:你真的相信「天下沒有白吃的午餐」這句話嗎？ <font color="blue">**正確**</font>

2. 

[第2張圖](input/2.png)
gemini_1.5_flash <font color="red">**錯2字，少5字**</font>
O:今天天氣很好，我們下午去公園散步。 <font color="blue">**正確**</font>
O:請在下午3點前，到A棟201號會議室開會。
X:請在下<font color="red">**課**</font><font color="green">**午3點**</font>前 <font color="green">**，**</font>到A棟201<font color="green">**號**</font>會議室開會。
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。
X:我辨認出<font color="red">**台**</font>灣的鳳梨酥包裝袋很精緻。
O:你真的相信「天下沒有白吃的午餐」這句話嗎？ <font color="blue">**正確**</font>

gemini_2.5_pro <font color="red">**多1字，少5字**</font>
O:今天天氣很好，我們下午去公園散步。
X:今天天氣很好，我們<font color="green">**下午**</font>去公園散步。
O:請在下午3點前，到A棟201號會議室開會。
X:請在下午3點前，到A棟201<font color="green">**號**</font>會議室開會。
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。 <font color="blue">**正確**</font>
O:你真的相信「天下沒有白吃的午餐」這句話嗎？
X:你真的相信<font color="green">**「**</font>天下沒有白吃的午餐<font color="green">**」**</font><font color="red">**，**</font>這句話嗎？

3. 

[第3張圖](input/3.png)

gemini_1.5_flash <font color="red">**錯1字**</font>
O:今天天氣很好，我們下午去公園散步 <font color="blue">**正確**</font>
O:請在下午3點前，到A棟201號會議室開會 <font color="blue">**正確**</font>
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。 <font color="blue">**正確**</font>
O:你真的相信「天下沒有白吃的午餐」這句話嗎？
X:<font color="red">**妳**</font>真的相信「天下沒有白吃的午餐」這句話嗎？

gemini_2.5_pro <font color="red">**有一句錯亂**</font>
O:今天天氣很好，我們下午去公園散步。 <font color="blue">**正確**</font>
O:請在下午3點前，到A棟201號會議室開會。 <font color="blue">**正確**</font>
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。 <font color="blue">**正確**</font>
O:你真的相信「天下沒有白吃的午餐」這句話嗎？
x秋天的楓橋下沒有南宮的字據，這句詩嗎？  <font color="red">**錯亂**</font>

4. 

[第4張圖](input/4.png)
gemini_1.5_flash<font color="blue">**全對**</font>
今天天氣很好，我們下午去公園散步。<font color="blue">**正確**</font>
請在下午3點前，到A棟201號會議室開會。<font color="blue">**正確**</font>
我辨認出臺灣的鳳梨酥包裝袋很精緻。<font color="blue">**正確**</font>
你真的相信「天下沒有白吃的午餐」這句話嗎？<font color="blue">**正確**</font>

gemini_2.5_pro <font color="red">**少2字，一句錯亂**</font>
O:今天天氣很好，我們下午去公園散步。
X:今天天氣很好，我們<font color="green">**下午**</font>去公園散步。
O:請在下午3點前，到A棟201號會議室開會。<font color="blue">**正確**</font>
X:請在下午3點前，到A棟201號會議室開會。
O:我辨認出臺灣的鳳梨酥包裝袋很精緻。
X:他親手為媽媽的圖書館裝設音響。<font color="red">**錯亂**</font>
O:你真的相信「天下沒有白吃的午餐」這句話嗎？<font color="blue">**正確**</font>

```

```

```

```
