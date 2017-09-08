python 默认编码格式是ASCII 所以一般对中文编码会产生问题，这就需要有一套专门的编码方法来处!
encode(params)就是处理编码的方法，像汉字这些编码肯定不会被ASCII支持，这就需要在输出python的文件之前把文件内容编码一下，编码成想要的内容然后输出到目的文件，相反，当从目标文件读取数据时候也要相应的根据目标文件的编码内容来解码decode(params),python 会把对应的内容转为python 需要的格式ASCII.
    所以在处理python编码问题上就保持 “一进一出原则”   一进的内容根据内容的编码格式转为python 内部格式（就是decode(params)）,一出的内容就根据目标需要的编码格式来编码 encode(params)

Params 参数就是编码和解码的具体格式  可以是’utf-8’ ，’gbk’ 等格式
