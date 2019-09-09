# 使用dask做分布式计算

dask是纯python的分布式科学计算框架,其旨在让熟悉python下数据科学工具的数据开发人员可以无痛的从单机版本的numpy,scipy,pandas,sklearn迁移到分布式计算,以适应大数据分析的需求,于此同时不失去python语言的灵活性.

dask的结构大致有3块:

+ 分布式的数据结构接口用于构造计算图
+ 调度器用于分发任务
+ worker运算节点