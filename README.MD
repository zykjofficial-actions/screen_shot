# 友链截图

## 介绍

本项目是基于 [ChenYFan](https://github.com/ChenYFan/ScreenShot) 大佬的项目修改而成、并参考 [baidu-url-submit-by-using-sitemap](https://github.com/jalenchuh/baidu-url-submit-by-using-sitemap) 的 `Github Action` 配置

截图网站为：https://www.thum.io/ 、具体使用可以查看官网官方文档：https://www.thum.io/documentation/api/url

使用`Python`获取`博客的友链`和`Gitee Issue的友链`并且截图

`Gitee Issue友链教程`：https://www.tzki.cn/posts/e01152f6/index.html (旧版)  https://www.yuque.com/kdoc/bf/friend (新版)

效果：

![](https://cdn.jsdelivr.net/gh/zykjofficial-actions/screen_shot@main/screen_shot.gif)

欢迎访问我的 [博客](https://zykj.js.org/link/) 查看效果

## 原理

通过 curl 命令下载图片、第一个命令图片大小比较小、第二个命令图片大小比较大

```
curl https://image.thum.io/get/width/400/crop/800/allowJPG/wait/20/noanimate/https://<YourDomain>/ -o <YourDoamin>.jpg

或者

curl https://image.thum.io/get/width/1024/crop/768/https://<YourDomain>/ -o <YourDoamin>.jpg
```

可以在 https://cdn.jsdelivr.net/gh/zykjofficial-actions/screen_shot@gh-pages/ 查看友链图片 **可能不适配** pjax

下载的图片参考了 [博客图片的 webp 之路](https://blog.ccknbc.cc/posts/the-webp-road-of-blog-pictures/#) 大佬的教程进行压缩

## 使用

fork `本仓库` 、~~在 https://github.com/settings/tokens  ，`Generate new token`、名字随便填、勾选 ` repo`、再点击`Generate token` 复制好token、在这个仓库`Settings > Secrets > new New secret`、Name 中填写 `TOKEN`，`Value` 为生成的token。(放入 Secrets 中能防止 token 泄露)~~ (默认存在一个TOKEN、可以不需要创建)

编辑 `screen_shot.py`

```python
if __name__ == '__main__':
    getLinkFriends("https://blog.zykjofficial.top/link/")
    getGiteeFriends("zykjofficial", "friends")
    downloadFriends()
```

- 将`getLinkFriends`函数里的内容替换成你自己的友链页面
- 将`getGiteeFriends`函数里替换成 `gitee用户名`、`ISSUE仓库`、如果你不使用`Gitee Issue友链`、请将这一行用`#`注释
- 如果你使用的是其他截图网站 API、`downloadFriends` 第一个参数为截图网站 API、格式类似 `https://image.thum.io/get/width/400/crop/800/allowJPG/wait/20/noanimate/`、第二个参数为下载图片的后缀 (默认 `jpg`), 或者类似 `https://s0.wordpress.com/mshots/v1/https://zykj.js.org?w=1280&h=960` 的 API、第一个参数为截图网站前缀 `https://s0.wordpress.com/mshots/v1/https://`、第二个参数为截图网站后缀 `?w=1280&h=960`、第三个参数为下载图片的后缀 (默认 `jpg`)

修改完成你的配置、就可以在Action查看是否运行成功

## 配置

`注意：此操作只支持Butterfly主题` ： 鼠标放在友链上可以显示友链截图

如果Butterfly主题开启了pjax、建议排除以免出现问题

```yml
pjax:
  enable: true
  exclude:
    - /link/ # link是我的友链页面
```

针对旧版 ：https://cdn.jsdelivr.net/gh/zykjofficial/zykjofficial.github.io@master/js/Friend_old.js

```html
<script src="https://cdn.jsdelivr.net/gh/zykjofficial/zykjofficial.github.io@master/js/Friend_old.js"></script>
<script src="https://cdn.jsdelivr.net/gh/zykjofficial-actions/screen_shot@main/screen_shot.js"></script>
<script>
    let fElement = document.createElement("div");
    fElement.id = "friend";
    document.querySelector(".flink").prepend(fElement);
    new Friend({
        el:"#friend",
        owner:"zykjofficial",
        repo:"friends",
        direction_sort:"asc",
        labelDescr:{
            "乐特专属":"<span style='color:red;'>这是乐特大佬的博客哟！</span>",
            "嘉神专属":"<span style='color:red;'>这是康特全球后援会(QQ群：939534493)的群主！</span>",
            "大佬们":"大佬们的博客(不分前后、都是大佬)",
            "傻逼菜狗":"一位隐藏的大佬",
            "Butterfly主题":"主题官网: <a link='https://butterfly.js.org'>https://butterfly.js.org</a> ",
        }
    })

    getFriendsScreenShot({
        user: "zykjofficial-actions", // github用户名
        repo: "screen_shot", // github仓库名
        branch: "gh-pages", //  分支: 可选参数(默认gh-pages分支)
        suffix: "jpg", // 图片后缀: 可选参数(默认jpg)
        lazyImg: "https://cdn.jsdelivr.net/gh/zykjofficial/zykjofficial.github.io@master/img/loading.gif", // 懒加载图片: 可选参数(默认https://cdn.jsdelivr.net/gh/zykjofficial/zykjofficial.github.io@master/img/loading.gif)
        duration: 5000 //Snackbar的持续时间: 可选参数(默认5000毫秒)
    })
</script>
```

针对新版：https://cdn.jsdelivr.net/npm/butterfly-friend@latest/dist/friend.min.js

```html
<script src='https://cdn.jsdelivr.net/npm/butterfly-friend@latest/dist/friend.min.js'></script>
<script src="https://cdn.jsdelivr.net/gh/zykjofficial/zykjofficial.github.io@master/js/screen_shot.js"></script>
<script>
  var obj = {
    el:"#friend1",
    owner:"zykjofficial",
    repo:"friends",
    direction_sort:"asc",
    sort_container:["乐特专属","大佬们"],
    labelDescr:{
        "乐特专属":"<span style='color:red;'>这是乐特大佬的博客哟！</span>",
        "嘉神专属":"<span style='color:red;'>这是康特全球后援会(QQ群：939534493)的群主！</span>",
        "大佬们":"大佬们的博客(不分前后、都是大佬)",
        "傻逼菜狗":"一位隐藏的大佬",
        "Butterfly主题":"主题官网: <a link='https://butterfly.js.org'>https://butterfly.js.org</a> ",
    }
  };
  document.querySelector('.flink').insertAdjacentHTML('afterbegin', "<div id='friend1'></div>")
  new Friend(obj)
  getFriendsScreenShot({
    user: "zykjofficial-actions", // github用户名
    repo: "screen_shot", // github仓库名
  })
</script>
```

添加`Snackbar`提示(确保Butterfly主题开启Snackbar)、当显示：`友链截图加载完毕` 就可以查看截图了、如果显示：`友链加载失败`，请刷新页面(有一定几率会加载失败)

## 何时运行

本项目会在`At 9:00 AM, only on Sunday`运行

如果想修改运行时间 、修改`screen_shot/.github/workflows/screen_shot.yml`

```yml
- cron: '0 0 * * 0'
```

 运行可能需要很长时间

## 问题

- 运行比较缓慢，毕竟下载图片需要一定时间
- 正则表达式写的太菜了、如果大佬有更好的改进、欢迎提Issue
- 部分网站的图片可能抓取不到

