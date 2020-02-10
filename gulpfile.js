const gulp = require("gulp");

const css = () => {
  const postCSS = require("gulp-postcss");
  const sass = require("gulp-sass");
  const minify = require("gulp-csso");
  sass.compiler = require("node-sass");
  return gulp
    .src("assets/scss/styles.scss") // 파일 찾기
    .pipe(sass().on("error", sass.logError))
    .pipe(postCSS([require("tailwindcss"), require("autoprefixer")])) // css tailwind rule  적용
    .pipe(minify()) // 코드 짧게 만들기
    .pipe(gulp.dest("static/css")); // static 디렉토리로 보내기
};

exports.default = css;
