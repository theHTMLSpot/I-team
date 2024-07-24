"use client";

import { useState, useEffect } from 'react';
import { usePathname } from 'next/navigation'; // Correct import for pathname
import Link from 'next/link';
import Image from 'next/image';
import styles from './navbar.module.css'; // Ensure this path is correct

const Navbar = () => {
  const pathname = usePathname(); // Get the current pathname

  const [currentPath, setCurrentPath] = useState<string>(pathname);

  useEffect(() => {
    setCurrentPath(pathname); // Update the current path when pathname changes
  }, [pathname]);

  return (
    <nav className={styles.navbar}>
      <ul className={styles.logoContainer}>
        <li className={styles.logo}>
          <Link href="/">
            <Image
              src="/logo.png"
              alt="Griftland College"
              width={100} // Adjust width as needed
              height={50} // Adjust height as needed
            />
          </Link>
        </li>
      </ul>
        
      <ul className={styles.navLinks}>
        <li className={currentPath === '/' ? styles.selected : ''}>
          <Link href="/">Home</Link>
        </li>
        <li className={currentPath === '/about' ? styles.selected : ''}>
          <Link href="/about">About</Link>
        </li>
        <li className={currentPath === '/agenda' ? styles.selected : ''}>
          <Link href="/agenda">Agenda</Link>
        </li>
        <li className={styles.cta}>
          <Link href="/join">Join Nu</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;