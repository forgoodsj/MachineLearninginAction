* ### DecisionTree 中文译名 决策树

* ### 优点：
> 计算复杂度不高，输出结果易于理解，对中间值的缺失不敏感，可以处理不相关特征数据。

* ### 缺点：
> 可能会产生过度匹配问题。

* ### 适用数据范围：
> 数值型和标称型

* ### 工作原理：
> 需要解决的第一个问题就是，当前数据集上哪个特征在划分数据分类时起到决定性作用。（根据信息增益判断）
>
> 分类后，如果数据子集内的数据不属于同一类型，则需要重复划分。

* ### 伪代码:
> 创建分支的伪代码行数createBranch()
>
> 检测数据集中的每个子项是否属于统一分类：
>
> >    if so return 类标签；
> >
> >    else
> >
> >       寻找划分数据集的最好特征
> >
> >       划分数据集
> >
> >       创建分支节点
> >
> >           for 每个划分的子集
> >
> >                  调用函数createBranch并增加返回结果到分支节点中
> >
> >      return 分支节点

* ### 若划分数据集时有多个特征，选择哪个特征作为划分的参考属性？
> 原则：将无序的数据变得更加有序。使用信息增益来衡量有序程度。

* ### 信息增益
> 在划分数据集之前之后信息发生的变化成为信息增益。我们可以计算每个特征值划分数据集获得的信息增益，获得信息增益最高的特征就是最好的选择。

* ### 创建决策树
> 生成一个代表树结构的前套字典，使用递归函数生成树
>
>
> 函数运行后，获取数据集中所有的标签
>
> >   如果如果数据集中所有的标签相同（第一个标签的数量等于列表长度），则停止划分，并返回该标签
> >
> >   如果使用完了所有特征，仍不能将数据集划分成仅包含唯一类别的分组，则选出现次数最多的标签作为返回值。
> >
> > >     通过函数获得最适合的分割的特征
> > >
> > >     创建一个该特征为key的字典
> > >
> > >    遍历该特征所有的标签
> > >
> >   对不同的标签执行上述操作（递归），直到退出

* ### 画出树

* ### 使用树进行分类
> 通过输入树， 特征标签，及特征标签对应的值的列表

* ### 存储树
> 以便后期重复使用

