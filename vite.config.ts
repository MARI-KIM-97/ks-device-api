import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  root: '.', // 현재 폴더를 루트로 사용
  build: {
    outDir: 'dist', // 결과물 생성 폴더를 'dist'로 설정
    emptyOutDir: true, // 빌드할 때 dist 폴더 비우기
  },
});
