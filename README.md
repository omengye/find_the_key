###题目

你的任务很简单，因为加密密钥是由三个小写字母组成的。文件 cipher1.txt包含了加密后的ASCII码，并且已知明文是由常用英语单词组成。使用该文件来解密信息，並最終獲取明文信息。  

###思路

由于从来没有接触过加密和解密之类的只是，所以做这道题的最开始的时候恶补了一下异或，不过还好，这个知识点还算是不太难。  
然后就想着还是用自己比较熟悉的python来做吧，google了下python里关于异或的一些方法。开始尝试用假设的密钥与密文的ascii异或进而得到明文。  
尝试了几个错误的密钥之后，发现了一些规律，由于题目中明确说明了关键点 **1，加密密钥是由三个小写字母组成的**，**2，明文是由常用英语单词组成**，从而可以尝试着通过判断符号（包括空格和各类型的标点符号）数目的多少来做这道题。有了这个思路之后，我在 test.py 这个文件中将“密文对应于三个小写字母组成的密钥”的将密文分为3个部分，然后计算出符号的数目（总字符数目 减去 字母数目）并从小到大排列，从而得到了以下结果:

	[('g', 94), ('d', 101), ('e', 103), ('a', 106), ('c', 107), ('f', 112), ('z', 130), ('x', 131), ('j', 140), ('m', 141), ('l', 143), ('b', 147), ('k', 149), ('q', 152), ('p', 161), ('v', 162), ('i', 164), ('w', 164), ('n', 171), ('y', 171), ('h', 176), ('r', 176), ('o', 181), ('s', 188), ('u', 192), ('t', 202)]
	[('o', 94), ('l', 99), ('m', 103), ('i', 105), ('h', 107), ('n', 114), ('k', 115), ('r', 129), ('j', 130), ('s', 131), ('b', 137), ('p', 139), ('e', 142), ('d', 144), ('a', 145), ('c', 152), ('q', 154), ('t', 155), ('w', 160), ('v', 164), ('y', 174), ('u', 175), ('f', 177), ('z', 182), ('x', 189), ('g', 200)]
	[('d', 97), ('g', 104), ('f', 106), ('b', 108), ('e', 115), ('c', 118), ('y', 128), ('x', 138), ('i', 145), ('a', 146), ('n', 146), ('h', 149), ('o', 152), ('r', 157), ('j', 161), ('s', 161), ('u', 162), ('z', 166), ('t', 168), ('q', 173), ('m', 184), ('l', 186), ('k', 191), ('v', 200), ('w', 202), ('p', 203)]

从得到的结果中来看，排列在前三位的'g','o','d'极有可能是我们要找的密钥，将假定的密钥'god'带入到 secret.py 中，果然，运气不错，看来'god'即为要找的密钥，解得的明文也自然得到了:

(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.
