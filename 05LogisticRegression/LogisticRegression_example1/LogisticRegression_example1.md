* ### 处理数据中的缺失值
> 可选的做法
>
> 1.使用可用特征的均值来填补缺失值。
>
> 2.使用特殊值来填补，例如-1
>
> 3.忽略有缺失值的样本
>
> 4.使用相似样本的均值填补缺失值
>
> 5.使用另外的机器学习算法预测缺失值

* ### 案例采取的方法
> 使用实数0来替换所有缺失值，恰好能用于逻辑回归。
>
> 当选中某特征对应值为0，则该系数将不做更新，同时sigmoid(0) = 0.5,对结果的预测不具有任何倾向性，因此也不会造成误差
>
> 如果发现一条数据的类别标签已经缺失，那么需要将该数据丢弃。