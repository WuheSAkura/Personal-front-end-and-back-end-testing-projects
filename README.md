
---

## 📘 Vue3 任务备忘录系统（Task Memo）

> 一个基于 Vue 3 + Vite 构建的轻量级任务备忘录前端系统，已成功部署上线。

---

### 🖼️ 项目预览

访问地址 👉 [http://8.138.250.37](http://8.138.250.37) （可根据你自己的服务器域名/IP 替换）

![项目预览图]([https://your-screenshot-url-if-needed.png](https://github.com/WuheSAkura/Personal-front-end-and-back-end-testing-projects/blob/renwu/%E5%89%8D%E7%AB%AF.jpg)) <!-- 可替换为项目截图地址 -->

---

### 🔧 项目功能

* ✅ 添加任务
* ✅ 标记任务为完成
* ✅ 删除任务
* ✅ 筛选任务（全部 / 未完成 / 已完成）
* ✅ 支持部署到 Nginx
* ✅ 响应式设计，适配桌面端浏览器

---

### 🧪 技术栈

| 技术                          | 说明                       |
| --------------------------- | ------------------------ |
| [Vue 3](https://vuejs.org/) | Composition API + SFC 组件 |
| [Vite](https://vitejs.dev/) | 极速前端构建工具                 |
| [Nginx](https://nginx.org/) | 用于静态资源部署                 |
| 原生 CSS                      | 组件内 `scoped style` 编写样式  |

---

### 🏗️ 本地运行步骤

```bash
# 克隆项目
git clone -b renwu https://github.com/WuheSAkura/Personal-front-end-and-back-end-testing-projects.git
cd vue3-todo

# 安装依赖
npm install

# 本地运行
npm run dev
```

---

### 🚀 项目构建并部署

```bash
# 构建生产版本
npm run build

# 构建后生成 dist/ 目录，可上传至服务器部署（如 Nginx）
```

---

### 📦 Nginx 推荐配置（示例）

```nginx
server {
    listen 80;
    server_name 你的IP或域名;

    root /路径/到/项目/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html =404;
    }
}
```

---

### 🙋‍♂️ 作者

| 作者         | GitHub                                       |
| ---------- | -------------------------------------------- |
| WuheSAkura | [@WuheSAkura](https://github.com/WuheSAkura) |

---

### 🌱 项目状态

> ✅ 已完成初始功能，欢迎 Star ⭐、Fork 🍴、部署！

---

### 📌 Todo List（未来计划）

* [ ] 本地存储任务（LocalStorage）
* [ ] 夜间模式 / 主题切换
* [ ] 音效提醒、任务时间设置
* [ ] 移动端样式优化

---

## ✅ LICENSE

MIT License

---


